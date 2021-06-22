from plugins.theme.bcolors import Bcolors 

class Welcome:
    def start(self): 
         print(f"""{Bcolors.OKBLUE}
                             ******    *******   *******   ******  
                            **////**  **/////** /**////** /*////** 
                            **    //  **     //**/**    /**/*   /** 
                            /**       /**      /**/**    /**/******  
                            /**       /**      /**/**    /**/*//// **
                            //**    **//**     ** /**    ** /*    /**
                            //******  //*******  /*******  /******* 
                            //////    ///////   ///////   ///////  {Bcolors.END}
                            DATABASE ADMINISTRATOR TOOL  -  BY EDWIN ARIZA
         """)