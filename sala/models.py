from django.db import models

class Salas(models.Model):
    UABJ = 'UABJ'
    AEB = 'AEB'

    LOCAL_CHOICES = [
        (UABJ, 'UABJ'),
        (AEB, 'AEB'),
    ]

    local = models.CharField(max_length=4, choices=LOCAL_CHOICES, default=UABJ)
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Sala'

    def __str__(self):
        return self.nome

class Reservas(models.Model):
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    pessoa = models.CharField(max_length=100)
    data_hora_reserva = models.DateTimeField()
    data_hora_devolucao = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Reserva'

    def __str__(self):
        return self.nome