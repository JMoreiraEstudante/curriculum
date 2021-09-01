from django.db import models

def user_directory_path(instance, filename):
    return 'projetos/{0}'.format(filename)

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, max_length=5000)
    linkGit = models.URLField(null=True)
    linkAcesso = models.URLField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    def get_id(self):
        return self.id

    def get_absolute_url(self):
        return "/projeto/%i/" % self.id

    def criaParagrafo(self):
        string = ''
        for paragrafo in self.descricao.split('\n'):
            string += "<p class='paragrafo'>{0}</p>".format(paragrafo)
        return string

    def criaCardDescricao(self):
        return self.descricao[0:80]+"..."

    def criaCodigoFonte(self):
        return "<p class='paragrafo'>Acesso o codigo fonte em: <a href="+self.linkGit+">"+self.linkGit+"</a></p>"
    
    def criaLinkAcesso(self):
        if self.linkAcesso is not None:
            return "<p class='paragrafo'>Link para a aplicação: <a href="+self.linkAcesso+">"+self.linkAcesso+"</a></p>"

    class Meta:
        ordering = ['-created_date']

class Foto(models.Model):
    image = models.ImageField(upload_to = user_directory_path)
    projeto =  models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='fotos')