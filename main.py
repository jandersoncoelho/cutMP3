from pydub import AudioSegment
from tqdm import tqdm
import os


# Função para dividir o áudio em partes e salvar como MP3
def dividir_audio(arquivo, duracao_corte):
    try:
        # Carregar o arquivo de áudio
        audio = AudioSegment.from_file(arquivo)

        # Calcular o número de cortes necessários
        duracao_total_ms = len(audio)
        duracao_corte_ms = duracao_corte * 60 * 1000  # Convertendo minutos para milissegundos
        num_cortes = duracao_total_ms // duracao_corte_ms

        # Obter o nome base do arquivo sem a extensão
        nome_base = os.path.splitext(os.path.basename(arquivo))[0]

        # Criar uma pasta para os novos arquivos MP3
        if not os.path.exists(nome_base):
            os.makedirs(nome_base)

        # Mensagem de início do processo
        print(f"Iniciando o processo de corte do arquivo {arquivo}...")

        # Loop para criar os cortes com barra de progresso
        for i in tqdm(range(num_cortes), desc="Cortando áudio"):
            # Definir o ponto inicial e final do corte
            inicio = i * duracao_corte_ms
            fim = inicio + duracao_corte_ms
            parte = audio[inicio:fim]
            # Salvar o arquivo na pasta criada
            parte.export(os.path.join(nome_base, f"parte_{i + 1}.mp3"), format="mp3")

        # Verificar se há um resto no final e criar um arquivo adicional se necessário
        resto = duracao_total_ms % duracao_corte_ms
        if resto > 0:
            parte_resto = audio[-resto:]
            parte_resto.export(os.path.join(nome_base, f"parte_{num_cortes + 1}.mp3"), format="mp3")

        # Mensagem de conclusão do trabalho
        print("O trabalho foi concluído com sucesso!")

    except FileNotFoundError:
        print("Erro: O arquivo de áudio especificado não foi encontrado.")
    except PermissionError:
        print("Erro: Permissão negada para acessar o arquivo ou diretório.")
    except IsADirectoryError:
        print("Erro: O caminho fornecido é um diretório, não um arquivo.")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")


if __name__ == '__main__':
    # Usar a função com o arquivo desejado e a duração de corte em minutos
    dividir_audio("caminho_para_seu_arquivo.wav", 28)
