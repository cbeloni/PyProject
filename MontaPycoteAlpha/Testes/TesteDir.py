#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pdb

# Verifica diretório
vDirAlpha = "~/Documentos/PyProjects/MontaPycoteAlpha/"
vDirProd  = "/opt/MontaPycote"
vVersao = "1" # 0 = Produção, 1 = alpha

#altera de acordo com vVersao
if vVersao == "0":
	vDir = vDirProd
else:
	vDir = vDirAlpha	
 
print os.system('dir ' + vDir) 
