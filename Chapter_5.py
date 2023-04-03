import numpy as np
import nnfs



class Loss:
  
    def calculate(self,output,y):
        
        sample_losses = self.forward(ouput,y)
        
        data_loss = np.mean(sample_losses)
        
        return data_loss
      
class Loss_CategoricalCrossEntropy(Loss):
    
    def forward(self,y_pred,y_true):
        
        samples = len(y_pred)
        
        y_pred_clipped
  
