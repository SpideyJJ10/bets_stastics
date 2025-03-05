import numpy as np
from scipy.stats import poisson

def main():
    teamA = input("Equipo elegido: ").strip()
    teamB = input("Equipo rival: ").strip()
    
    # Obtener datos de ataque y defensa, localía y forma
    teamA_attack, teamA_defense, home_advantage_A, form_A, injuries_A = get_team_data(teamA, local=True)
    teamB_attack, teamB_defense, home_advantage_B, form_B, injuries_B = get_team_data(teamB, local=False)
    
    # Ajustar goles esperados por localía, forma y lesiones
    expected_goals_A = (teamA_attack * teamB_defense) * home_advantage_A * form_A * injuries_A
    expected_goals_B = (teamB_attack * teamA_defense) * home_advantage_B * form_B * injuries_B

    print(f"\n🔹 Goles esperados: {teamA} ({expected_goals_A:.2f}) vs {teamB} ({expected_goals_B:.2f})")
    
    # Simular posibles marcadores con los factores extra
    simulate_match(expected_goals_A, expected_goals_B, teamA, teamB)

def get_team_data(team, local):
    """Obtiene datos de ataque, defensa y factores extra."""
    avg_goals_scored = float(input(f"⚽ Promedio de goles anotados por {team}: "))
    avg_goals_conceded = float(input(f"🛑 Promedio de goles concedidos por {team}: "))
    
    # Factor Localía (1.15 si es local, 0.85 si es visitante)
    home_advantage = 1.15 if local else 0.85
    
    # Factor Forma (Basado en los últimos 5 partidos)
    last_5_matches = input(f"📊 Últimos 5 partidos de {team} (ejemplo: WWLDL): ").upper()
    form_factor = calculate_form_factor(last_5_matches)

    # Factor de Lesiones/Sanciones (1.0 si está completo, menor si tiene bajas)
    injuries = int(input(f"🚑 Número de jugadores clave ausentes en {team}: "))
    injuries_factor = 1.0 - (injuries * 0.05)  # Cada baja reduce un 5% el rendimiento

    return avg_goals_scored, avg_goals_conceded, home_advantage, form_factor, injuries_factor

def calculate_form_factor(last_5):
    """Convierte los últimos 5 partidos en un factor numérico."""
    points = {'W': 1.1, 'D': 1.0, 'L': 0.9}  # Win = 1.1, Draw = 1.0, Loss = 0.9
    return np.mean([points.get(match, 1.0) for match in last_5])

def simulate_match(lambda_A, lambda_B, teamA, teamB):
    """Simula la probabilidad de cada marcador basado en Poisson con factores adicionales."""
    print("\n📊 Probabilidades de marcadores más probables:")
    for gA in range(4):
        for gB in range(4):
            prob = poisson.pmf(gA, lambda_A) * poisson.pmf(gB, lambda_B)
            print(f"{teamA} {gA} - {gB} {teamB}: {prob*100:.2f}%")

main()
