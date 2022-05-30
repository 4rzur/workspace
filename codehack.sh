#!/bin/bash

clear
echo -e "### Programa de codificación de textos ###\n\n"

echo -e "Introduce el texto a codificar: \n\n"
read TEXTO
sleep 2
echo -e "\n$TEXTO" | tr 'aelosAOESLB'   '43105403518'

exit


#by WOPR

