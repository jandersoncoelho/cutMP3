from pydub import AudioSegment


# Função para dividir o áudio em partes e salvar como MP3
def dividir_audio(arquivo, duracao_corte):
    # Carregar o arquivo de áudio
    audio = AudioSegment.from_file(arquivo)

    # Calcular o número de cortes necessários
    duracao_total_ms = len(audio)
    duracao_corte_ms = duracao_corte * 60 * 1000  # Convertendo minutos para milissegundos
    num_cortes = duracao_total_ms // duracao_corte_ms  # Usando divisão inteira para evitar cortes extras

    # Loop para criar os cortes
    for i in range(num_cortes):
        # Definir o ponto inicial e final do corte
        inicio = i * duracao_corte_ms
        fim = inicio + duracao_corte_ms
        parte = audio[inicio:fim]
        parte.export(f"parte_{i + 1}.mp3", format="mp3")

    # Verificar se há um resto no final e criar um arquivo adicional se necessário
    resto = duracao_total_ms % duracao_corte_ms
    if resto > 0:
        parte_resto = audio[-resto:]
        parte_resto.export(f"parte_{num_cortes + 1}.mp3", format="mp3")


if __name__ == '__main__':
    # Usar a função com o arquivo desejado e a duração de corte em minutos
    dividir_audio("Ednan-Corretor-de-(03432141396)_20240404142233.mp3", 28)
