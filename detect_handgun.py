import cv2
import os

from ultralytics import YOLO


def most_recent_model():
    final_path = ""
    
    current_path = os.getcwd()
    model_folder_path = os.path.join(current_path, "model")
    
    max_run = 0
    if len(os.listdir(model_folder_path)) != 0:
        for folder in os.listdir(model_folder_path):
            if folder[:3] == "run":
                run_no = int(str(folder).split("_")[-1])
                if run_no>max_run:
                    max_run = run_no
            else:
                print("non run file detected")
        max_run_path = os.path.join(model_folder_path, f"runs_{max_run}")
            
        if len(os.listdir(max_run_path)) != 0:
            for file in os.listdir(max_run_path):
                if file == "detect":
                    detect = True
                    break
                else:
                    detect = False
        else:
            print("max run file empty.")
            
        if detect == True:
            train_file_path = os.path.join(max_run_path, "detect")
        else:
            train_file_path = os.path.join(max_run_path)
            
        max_train = 0
        for train in os.listdir(train_file_path):
            if train[:5] == "train":
                if train[-1] != "n":
                    train_no = int(train[-1])
                    if train_no > max_train:
                        max_train = train_no
            else:
                print("non train file detected.")
                
        if train_no>0:
            if train == 1:
                max_train_path = os.path.join(train_file_path, "train")
            else:
                max_train_path = os.path.join(train_file_path, f"train{max_train}")
        else:
            print("no train file in max run")
        
        final_path = os.path.join(max_train_path, "weights", "best.pt")
        return final_path
    else:
        print("no run folder found")
    
    
    
    