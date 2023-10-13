import '@/styles/globals.css'
import type { AppProps } from 'next/app'

//query
import { useQueryClient, QueryClientProvider, QueryClient } from '@tanstack/react-query'
import { Provider } from 'jotai'
import { queryClientAtom } from 'jotai-tanstack-query'
import {useHydrateAtoms} from 'jotai/react/utils'

const queryClient = new QueryClient()

const HydrateAtoms = ({children} : any) => {
  useHydrateAtoms([[queryClientAtom, queryClient]])
  return children
}



export default function App({ Component, pageProps }: AppProps) {
  return (
    <QueryClientProvider client={queryClient}>
      <Provider>
        <HydrateAtoms>
          <Component {...pageProps} />
        </HydrateAtoms>
      </Provider>
    </QueryClientProvider>
  )

}
