import axios from 'axios'

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const promptService = {
  async optimizePrompt({ background, role, expectation }) {
    const response = await apiClient.post('/prompt/optimize', {
      background,
      role,
      expectation,
    })
    return response.data
  },
}
