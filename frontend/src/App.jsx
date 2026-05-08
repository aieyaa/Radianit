import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [agents, setAgents] = useState([])

  useEffect(() => {
    fetch('/api/agents/')
      .then(res => res.json())
      .then(data => setAgents(data))
      .catch(err => console.error("Erreur lors de la récupération des agents:", err))
  }, [])

  return (
    <div className="App">
      <header className="hero">
        <div className="hero-content fade-in">
          <h1 className="hero-title">Radianit</h1>
          <p className="hero-subtitle">Le Hub Valorant Propulsé par Django & React</p>
          <div className="cta-group">
            <button className="btn btn-primary" onClick={() => setCount(count + 1)}>
              Explorez les Agents ({count})
            </button>
            <button className="btn btn-outline" style={{ marginLeft: '1rem' }}>
              Statistiques
            </button>
          </div>
        </div>
      </header>

      <main className="container">
        <section className="glass-card fade-in" style={{ marginTop: '-100px', marginBottom: '4rem' }}>
          <h2 style={{ color: 'var(--primary)', marginBottom: '1rem' }}>Bienvenue sur Radianit</h2>
          <p>
            Cette application est connectée à une API Django. Voici les agents récupérés en temps réel :
          </p>
        </section>

        <section className="grid" style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
          gap: '2rem',
          paddingBottom: '4rem'
        }}>
          {agents.map(agent => (
            <div key={agent.id} className="glass-card fade-in" style={{ textAlign: 'left' }}>
              <h3 style={{ color: 'var(--primary)', textTransform: 'uppercase' }}>{agent.name}</h3>
              <p style={{ opacity: 0.7 }}>Rôle : {agent.role}</p>
              <p style={{ opacity: 0.7 }}>Origine : {agent.country}</p>
            </div>
          ))}
          {agents.length === 0 && <p>Chargement des agents...</p>}
        </section>
      </main>

      <footer style={{ padding: '2rem', textAlign: 'center', opacity: 0.5 }}>
        <p>&copy; 2024 Radianit Project - Made with ❤️ by Antigravity</p>
      </footer>
    </div>
  )
}

export default App
