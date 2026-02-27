class Olla:
    
    def _init_(self,agua):
        self._agua = agua
    
    def cocinar_pasta(self,pasta):
        if self._agua._temperatura ==100:
            pasta.cocinar()
        else:
            print("el agua no esta hirviendo")