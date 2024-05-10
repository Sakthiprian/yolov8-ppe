# YOLOv8 PPE Detection

This repository contains a YOLOv8-based model for detecting personal protective equipment (PPE) using ONNX for CPU inference and TensorRT for GPU inference, aimed at speeding up inference time.

## Installation

1. Clone the GitHub repository.

2. Install required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

### 1. Convert Annotations (Optional)

If your annotations are in Pascal VOC format and you need them in YOLO format, you can use the provided script:

```
python pascaltoVOC_to_YOLO.py "path_to_input_folder" "path_to_output_folder"
```


### 2. Split Dataset (Optional)

To split your dataset into training and validation sets, use the train_validation_split.py file


### 3. Train Model on Custom Dataset (Optional)

If you have a custom dataset and want to train the model:

- Use the provided Jupyter notebook.
- Replace the path of the configuration file and the model with your custom paths.

### 4. Download the weights and place them in weights folder

 - Download the weights for the detection model and upload them in weights folder. Use ONNX for faster CPU inference and tensorRT for faster GPU inference

### 5. Run Inference

To perform inference using the trained model:


- If using default models and folder paths, simply run:

    ```
    python inference.py
    ```

Place the images in the `test_inputs` folder. Results will be available at `test_outputs` by default.

- If using custom settings, run:
    ```
    python inference.py -i "path_to_input_directory" -o "path_to_outputs_directory" --person_model "path_to_person_detection_model" --ppe_model "path_to_ppe_detection_model"
    ```

## License

This project is licensed under the [MIT License](LICENSE).
