# Extract bounding boxes
    boxes = results[0].boxes.xyxy.tolist()
    ultralytics_crop_object_list = []
    # Iterate through the bounding boxes
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box
        # Crop the object using the bounding box coordinates
        crop_img = img[int(y1):int(y2), int(x1):int(x2)]
        ultralytics_crop_object_list.append(crop_img)
        # Save the cropped image
        output_filename = f"{file.split('.')[0]}_person_{i}_cropped.jpg"
        output_filepath = os.path.join(args.o, output_filename)
        cv2.imwrite(output_filepath, crop_img)

    # Iterate through cropped objects
    for i, crop_img in enumerate(ultralytics_crop_object_list):
        ppe_res = model_ppe.predict(crop_img)
        boxes_ppe = ppe_res[0].boxes.xyxy.tolist()
        classes_ppe = ppe_res[0].boxes.cls.tolist()
        conf_ppe = ppe_res[0].boxes.conf.tolist()
        for j, ppe_box in enumerate(boxes_ppe):
            px1, py1, px2, py2 = ppe_box
            # Adjusting coordinates for the full image
            px1 += int(boxes[i][0])
            px2 += int(boxes[i][0])
            py1 += int(boxes[i][1])
            py2 += int(boxes[i][1])
            # Draw bounding box and text on the full image
            cv2.rectangle(img, (int(px1), int(py1)), (int(px2), int(py2)), color=(0, 0, 255), thickness=2)
            text_position = (int(px1), int(py1) + 10)  # Adjusting y-coordinate for placing text above the box
            classname = class_mapping_inverse[int(classes_ppe[j])]
            cv2.putText(img, text=str(str(round(conf_ppe[j], 2)) + " " + classname), org=text_position, fontFace=1, fontScale=0.6, color=(255, 0, 0), thickness=1)

    # Save the image with bounding boxes to the output folder
    output_filename = f"{file.split('.')[0]}_with_bounding_boxes.jpg"
    output_filepath = os.path.join(args.o, output_filename)
    cv2.imwrite(output_filepath, img)
