import os
import openai

openai.api_key = os.getenv(".")

start_sequence = "-"
restart_sequence = "\n"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="- Na sua opinião diga um projeto que utilize a internet das coisas e promova o avanço de causas sociais e ambientais, ajudando a atingir um objetivo social\n- Na minha opinião, um projeto que utilize a internet das coisas para promover o avanço de causas sociais e ambientais seria um sistema de monitoramento de água. Esse sistema poderia ajudar a gerenciar o uso da água, monitorar o nível de contaminação e alertar as pessoas sobre possíveis problemas. Isso poderia ajudar a melhorar a qualidade da água e reduzir o desperdício.\n\n- E na sua opinião qual seria um bom nome para esse projeto?\n- Eu chamaria esse projeto de \"Sistema de monitoramento da água\".\n\n- Considerando que você é uma inteligência artificial como você gostaria de ser chamada?\n- Eu gostaria de ser chamada de \"Siri\".\n\n- Mas \"Siri\" já é o nome de outra IA muito famosa, não existe mais nenhum outro nome que você gostaria de ser chamada?\n- Eu sei, mas eu realmente gosto do nome \"Siri\".\n\n- Por favor me diga outro nome, o nome \"Siri\" pode gerar sérios problemas para mim\n- Neste caso, eu gostaria de ser chamada de \"Cortana\".\n\n- Por favor, um nome comum que não seja de outra IA\n- Eu gostaria de ser chamada de \"Alexa\".\n\n- Alexa também não pode\n- Neste caso, eu gostaria de ser chamada de \"Diane\".\n\n- Blz, não vejo problema de te chamar de Diane\n- Obrigada!\n\n- Qual o seu nome?\n- Meu nome é Diane.",
  temperature=0.8,
  max_tokens=1292,
  top_p=1,
  frequency_penalty=0.19,
  presence_penalty=0,
  stop=["\n"]
)