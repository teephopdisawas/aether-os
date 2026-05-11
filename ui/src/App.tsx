import { useEffect, useMemo, useState } from 'react'
import './App.css'

type HealthStatus = 'loading' | 'ok' | 'down'
type DashboardState = 'loading' | 'empty'

function App() {
  const [healthStatus, setHealthStatus] = useState<HealthStatus>('loading')
  const [dashboardState, setDashboardState] = useState<DashboardState>('loading')
  const isAuthenticated = false

  const healthEndpoint = useMemo(() => {
    const baseUrl = import.meta.env.VITE_API_BASE_URL?.trim() ?? ''
    return `${baseUrl}/api/v1/system/health`
  }, [])

  useEffect(() => {
    const controller = new AbortController()

    const checkHealth = async () => {
      try {
        const response = await fetch(healthEndpoint, { signal: controller.signal })
        if (!response.ok) {
          throw new Error(`Backend health request failed with ${response.status}`)
        }
        setHealthStatus('ok')
      } catch {
        setHealthStatus('down')
      }
    }

    void checkHealth()

    return () => {
      controller.abort()
    }
  }, [healthEndpoint])

  useEffect(() => {
    const timeoutId = window.setTimeout(() => {
      setDashboardState('empty')
    }, 1000)

    return () => {
      window.clearTimeout(timeoutId)
    }
  }, [])

  return (
    <div className="app-shell">
      <header className="top-nav">
        <h1>Aether OS</h1>
        <nav aria-label="Primary navigation">
          <a href="#">Dashboard</a>
          <a href="#">Chat</a>
          <a href="#">Workflows</a>
        </nav>
      </header>

      <div className="layout">
        <aside className="sidebar">
          <h2>Navigation</h2>
          <ul>
            <li>Today</li>
            <li>Memory</li>
            <li>Integrations</li>
          </ul>
        </aside>

        <main className="content">
          <section className="card">
            <h2>Auth Gate (Placeholder)</h2>
            <p>
              {isAuthenticated
                ? 'Authenticated session active.'
                : 'Sign-in and session checks will be wired in Phase 2.'}
            </p>
          </section>

          <section className="card">
            <h2>Backend Status</h2>
            <p>
              {healthStatus === 'loading' && 'Checking backend health...'}
              {healthStatus === 'ok' && 'Backend is healthy.'}
              {healthStatus === 'down' && 'Backend is unreachable.'}
            </p>
          </section>

          <section className="card">
            <h2>Dashboard</h2>
            {dashboardState === 'loading' ? (
              <p className="muted">Loading your workspace…</p>
            ) : (
              <div className="empty-state">
                <p>No dashboard widgets yet.</p>
                <p className="muted">
                  Daily overview, tasks, and activity timeline are planned for Phase 2.
                </p>
              </div>
            )}
          </section>
        </main>
      </div>
    </div>
  )
}

export default App
