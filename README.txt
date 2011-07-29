
###################################################
## Author: Nicola Di Giorgio
## Name: BinManager
## Description: A multi-fold tool for the binary file deployment. In particular, the following functionality: upgrade, zip, 				monitor timestamp, prepare files for translation
## Updated 12 September 2011
###################################################


BinManager 1.0.4d

-Improved the translation part
-TransFiles.xml updated with new files


BinManager 1.0.4c

- Support x64 via attribute x64=yes
- New attribute zipTarget
- The opt=alerter moves directly to the Alerter. It can be use for the startup



 Usage: [-src=source] [-trg=target] [-alertDir=folder1;folder2;... folders for the BinAlerter]
        [-zipTarget=target for the Zipper] [-transDir=ToBeTranslated folder]
        [-opt= option: 'copy','zip','alerter','trans'] [-sound=yes|no]
        [-popup=yes|no] [-delay= delay of the BinAlerter] [-x64=yes|no]