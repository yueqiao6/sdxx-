from ultralytics import YOLO

def main():
    # Load a model
    model = YOLO("best.pt")

    # Train the model
    train_results = model.train(
        data="F:/v11/ultralytics-main/datas/data.yaml",  # path to dataset YAML
        epochs=1,  # number of training epochs
        imgsz=640,  # training image size
        device="0",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
    )

    # Evaluate model performance on the validation set
    metrics = model.val()
if __name__ == '__main__':
    main()
