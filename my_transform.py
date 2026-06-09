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
        