from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from my_transform import My_Transform
import sys

from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    
)

sys.modules['__main__'].My_Transform = My_Transform

loaded_model=joblib.load("models/xgb_final_pipeline_deploy.pkl")





class Predict_Sample(BaseModel):
    Age:float
    Height:float
    Weight:float
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
    final_prediction_proba=loaded_model.predict_proba(df_data_predict)[:,1][0]
    final_prob = round(float(final_prediction_proba) * 100, 2)
    return {
        "response_result":int(final_prediction[0]),
        "response_proba":final_prob
            
            }
    
        