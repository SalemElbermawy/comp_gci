from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from sklearn.base import BaseEstimator, TransformerMixin




class My_Transform(BaseEstimator,TransformerMixin):
    
    def __init__(self,Press_Rate=True,BMI=True,Speed_Ratio=True,Jump_Power=True,Power=True):
        self.Press_Rate=Press_Rate
        self.BMI=BMI
        self.Speed_Ratio=Speed_Ratio
        self.Jump_Power=Jump_Power
        self.Power=Power
    def fit(self,X,y=None):
        return self
    
    def transform (self,X):
        X=X.copy()
        if self.BMI:
            X["BMI"]=X["Weight"]/(X["Height"]**2)
        if self.Press_Rate:
            X["Press_Rate"] = X["Bench_Press_Reps"] / X["Weight"]
        if self.Speed_Ratio:
            
            X["Speed_Ratio"]=X["Weight"]/X["Sprint_40yd"]
            
        if self.Jump_Power:
            
            X["Jump_Power"]= X["Vertical_Jump"] * X["Broad_Jump"]
        
        if self.Power:
            
            X["Power"] = X["Sprint_40yd"] * X["Vertical_Jump"] * X["Broad_Jump"]
        
        return X
        
        
loaded_model=joblib.load("models/xgb_final_pipeline_deploy.pkl")


app=FastAPI()


class Predict_Sample(BaseModel):
    Age:float
    Height:float
    Sprint_40yd:float
    Vertical_Jump:float
    Bench_Press_Reps:float
    Broad_Jump:float
    Player_Type:str
    Position_Type:str

@app.post("/model")

def prediction(sample:Predict_Sample):
    
    sample=dict(sample)
    
    df_data_predict=pd.DataFrame([sample])
    
    final_prediction=loaded_model.predict(df_data_predict)
    
    return {"response":final_prediction}
    
        