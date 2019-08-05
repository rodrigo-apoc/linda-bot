#! python3
# -*- coding: utf-8 -*

import sys,os,aiml

### Carregar a IA
kernel = aiml.Kernel()

### Condicional para procurar o arquivo "cérebro" do BOT, SE existir ele vai carregar a base de conhecimento já existente.
if os.path.isfile("bot_brainIRC.brn"):
    kernel.bootstrap(brainFile = "bot_brainIRC.brn")
else:
    kernel.bootstrap(learnFiles = "startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brainIRC.brn")