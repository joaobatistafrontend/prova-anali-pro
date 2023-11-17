from django.db import models
from django.contrib.auth.models import User

class ArtModel(models.Model):
    PARTICIPACAO_CHOICES = [
        ('cliente', 'Cliente'),
        ('tecnico', 'Técnico'),
        ('engenheiro', 'Engenheiro'),
        ('fiscal', 'Fiscal'),
        # Adicione outras opções conforme necessário
    ]

    participacao = models.CharField(max_length=20, choices=PARTICIPACAO_CHOICES)
    motivos = models.TextField()
    dados_contratante = models.TextField()
    anexos = models.FileField(upload_to='anexos/')
    normas_compliance = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ART para {self.dados_contratante} - {self.user.username}"
