import time
from datetime import datetime, timedelta

# Lista de quartos para o rodízio
quartos = [912, 913, 930, 904, 905, 906, 908]

# Nome do arquivo para armazenar o índice do rodízio
indice_arquivo = "rodizio_faxina.txt"

def carregar_indice():
    """Carrega o índice atual do rodízio do arquivo."""
    try:
        with open(indice_arquivo, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0  # Começa do início da lista se o arquivo não existir

def salvar_indice(indice):
    """Salva o índice atual do rodízio no arquivo."""
    with open(indice_arquivo, "w") as file:
        file.write(str(indice))

def exibir_mensagem(quarto):
    """Exibe a mensagem para o rodízio."""
    mensagem = f"Hoje é a vez do quarto {quarto} realizar a faxina no alojamento."
    print(mensagem)

def rodizio():
    """Executa o rodízio de faxina."""
    indice = carregar_indice()
    quarto_atual = quartos[indice]
    
    # Exibe a mensagem para o quarto do dia
    exibir_mensagem(quarto_atual)
    
    # Atualiza o índice para o próximo dia
    indice = (indice + 1) % len(quartos)
    salvar_indice(indice)

def agendar_execucao(horario):
    """Agenda a execução do rodízio em um horário específico."""
    while True:
        agora = datetime.now()
        proximo_horario = datetime.combine(agora.date(), horario)
        if agora > proximo_horario:
            proximo_horario += timedelta(days=1)
        
        # Calcula o tempo de espera até o próximo horário
        tempo_espera = (proximo_horario - agora).total_seconds()
        print(f"Próxima execução às {proximo_horario.strftime('%H:%M:%S')} (em {tempo_espera:.0f} segundos)")
        
        # Aguarda até o horário especificado
        time.sleep(tempo_espera)
        
        # Executa o rodízio
        rodizio()

# Configuração: Defina o horário para o rodízio
if __name__ == "__main__":
    horario_fixo = datetime.strptime("08:00", "%H:%M").time()  # Ajuste o horário aqui
    agendar_execucao(horario_fixo)
