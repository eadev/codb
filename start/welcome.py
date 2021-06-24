from plugins.theme.bcolors import Bcolors
from conf.usuario import Usuario
class Welcome:
    def start(self): 
        # CREAMOS EL ARCHIVO DE CONFIGURACIÓN
        ousuario = Usuario()
        ousuario.establecer_home()
        ousuario.crear_config()
        # MOSTRAMOS EL MENSAJE DE BIENVENIDA
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
                        URL: https://github.com/eadev/codb
        """)