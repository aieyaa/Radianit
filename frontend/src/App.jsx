import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [agents, setAgents] = useState([])
  const [armes, setArmes] = useState([])
  const [maps, setMaps] = useState([])
  const [powers, setPowers] = useState([])
  const [showModal, setShowModal] = useState(false)

  // Chargement des agents
  useEffect(() => {
    fetch('/api/agents/')
      .then(res => res.json())
      .then(data => setAgents(data))
      .catch(err => console.error("Erreur lors de la récupération des agents:", err))

    fetch('/api/armes/')
      .then(res => res.json())
      .then(data => setArmes(data))
      .catch(err => console.error("Erreur lors de la récupération des armes:", err))

    fetch('/api/maps/')
      .then(res => res.json())
      .then(data => setMaps(data))
      .catch(err => console.error("Erreur lors de la récupération des cartes:", err))

    fetch('/api/powers/')
      .then(res => res.json())
      .then(data => setPowers(data))
      .catch(err => console.error("Erreur lors de la récupération des pouvoirs:", err))
  }, [])

  // Modal première visite
  useEffect(() => {
    const alreadySeen = localStorage.getItem('welcome-modal')

    if (!alreadySeen) {
      setShowModal(true)
      localStorage.setItem('welcome-modal', 'true')
    }
  }, [])

  return (
    <div className="App">

      {/* MODAL */}
      {showModal && (
        <div className="modal-overlay">
          <div className="modal">
            <h2>Bienvenue sur Radianit 👋</h2>
            <p>
              Découvrez Valorant <br />
              Ce site a pour unique objectif de fournir des informations et du contenu à titre informatif. 
              Il ne s’agit en aucun cas d’une copie, d’une imitation officielle ou d’un remplacement du site original. 
              Toutes les marques, noms et contenus mentionnés restent la propriété de leurs détenteurs respectifs.  
              Cette démarche est indépendante et vise uniquement à présenter des informations de manière claire et accessible.
            </p>

            <button
              className="btn btn-primary"
              onClick={() => setShowModal(false)}>
              Parfait, continuons
            </button>
          </div>
        </div>
      )}

      <header className="hero">
        <div className="hero-content fade-in">
          <h1 className="hero-title">Radianit</h1>
          <p className="hero-subtitle">
            Le Hub Valorant Propulsé par Django & React
          </p>

          <div className="cta-group">
            <button
              className="btn btn-primary"
              onClick={() => setCount(count + 1)}
            >
              Explorez les Agents ({count})
            </button>

            <button
              className="btn btn-outline"
              style={{ marginLeft: '1rem' }}
            >
              Statistiques
            </button>
          </div>
        </div>
      </header>

      <main className="container">
        <section
          className="glass-card fade-in"
          style={{
            marginTop: '-100px',
            marginBottom: '4rem'
          }}
        >
          <h2
            style={{
              color: 'var(--primary)',
              marginBottom: '1rem'
            }}
          >
            Bienvenue sur Radianit
          </h2>

          <p>
            Cette application est connectée à une API Django.
            Voici les agents récupérés en temps réel :
          </p>
        </section>

        <section
          className="grid"
          style={{
            display: 'grid',
            gridTemplateColumns:
              'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '2rem',
            paddingBottom: '4rem'
          }}
        >
          {agents.map(agent => (
            <div
              key={agent.id}
              className="glass-card fade-in"
              style={{ textAlign: 'left' }}
            >
              <h3
                style={{
                  color: 'var(--primary)',
                  textTransform: 'uppercase'
                }}
              >
                {agent.name}
              </h3>

              <p style={{ opacity: 0.7 }}>
                Rôle : {agent.role}
              </p>

              <p style={{ opacity: 0.7 }}>
                Origine : {agent.country}
              </p>
            </div>
          ))}

          {agents.length === 0 && (
            <p>Chargement des agents...</p>
          )}
        </section>

        <section>
          <h2>Armes</h2>
          {armes.map(arme => (
            <div
              key={arme.id}
              className="glass-card fade-in"
              style={{ textAlign: 'left' }}
            >
              <h3
                style={{
                  color: 'var(--primary)',
                  textTransform: 'uppercase'
                }}
              >
                {arme.title}
              </h3>

              <p style={{ opacity: 0.7 }}>
                {arme.content}
              </p>
            </div>
          ))}

          {armes.length === 0 && (
            <p>Chargement des armes...</p>
          )}
        </section>

        <section>
          <h2>Cartes</h2>
          {maps.map(carte => (
            <div
              key={carte.id}
              className="glass-card fade-in"
              style={{ textAlign: 'left' }}
            >
              <h3
                style={{
                  color: 'var(--primary)',
                  textTransform: 'uppercase'
                }}
              >
                {carte.name}
              </h3>

              <p style={{ opacity: 0.7 }}>
                {carte.description}
              </p>
            </div>
          ))}

          {maps.length === 0 && (
            <p>Chargement des cartes...</p>
          )}
        </section>

        <section>
          <h2>Pouvoirs</h2>
          {powers.map(power => (
            <div
              key={power.id}
              className="glass-card fade-in"
              style={{ textAlign: 'left' }}
            >
              <h3
                style={{
                  color: 'var(--primary)',
                  textTransform: 'uppercase'
                }}
              >
                {power.name}
              </h3>

              <p style={{ opacity: 0.7 }}>
                {power.description}
              </p>
            </div>
          ))}

          {powers.length === 0 && (
            <p>Chargement des pouvoirs...</p>
          )}
        </section>
      </main>



      <footer
        style={{
          padding: '2rem',
          textAlign: 'center',
          opacity: 0.5
        }}
      >
        <p>
          &copy; 2024 Radianit Project - Made with ❤️ by Antigravity
        </p>
      </footer>
    </div>
  )
}

export default App