import Image from 'next/image'
import { Inter } from 'next/font/google'
import { useAtom } from 'jotai'
import { atomsWithQuery } from 'jotai-tanstack-query'
import { atom } from 'jotai'
import { useEffect } from 'react'

const inter = Inter({ subsets: ['latin'] })

const idAtom = atom(3)
const [userAtom] = atomsWithQuery((get) => ({
  queryKey: ['users', get(idAtom)],
  queryFn: async ({ queryKey: [, id] }) => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    return res.json()
  },
}))

const UserData = () => {
  const [data] = useAtom(userAtom)
  return <div>{JSON.stringify(data)}</div>
}

export default function Home() {


  return (
    <>
      <UserData />
      <h1>HELLO</h1>
    </>
  )
}
