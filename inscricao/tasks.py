from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from PIL import Image, ImageDraw
import os
from hashlib import sha256

@shared_task
def cria_convite(nome, email):
    template = os.path.join(settings.STATIC_ROOT, 'img/convite_fundo_transparente.png')
    img = Image.open(template)
    img_escrever = ImageDraw.Draw(img)
    img_escrever.text((40, 270), nome, fill=(200, 89, 255))
    chave_secreta = "FASDJKFH#$#2%$dfdkjksdfHJF4541@&SDFDFJKhdfjg"  
    token = sha256((email + chave_secreta).encode()).hexdigest()
    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    img.save(path_salvar)
    send_mail('CADASTRO CONFIRMADO', f'Seu cadastro foi confirmado com sucesso (task) \n Aqui está o link do seu convite: http://127.0.0.1:8000/media/convites/{token}.png', 'caio@pythonando.com.br', recipient_list=[email])
    