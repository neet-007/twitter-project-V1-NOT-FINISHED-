import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import {BrowserRouter} from 'react-router-dom'
import {QueryClient, QueryClientProvider} from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import './assets/index.css'

const queryClinet = new QueryClient()
ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
   <QueryClientProvider client={queryClinet}>
    <React.StrictMode>
        <App />
        <ReactQueryDevtools/>
      </React.StrictMode>,
   </QueryClientProvider>
  </BrowserRouter>
)
