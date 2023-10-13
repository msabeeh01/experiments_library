import Image from 'next/image'
import { Inter } from 'next/font/google'

//store import
import { useBearStore } from '@/stores/bearStore'
import Link from 'next/link'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const bears = useBearStore()
  return (
    <>
      <h1>{bears.bears}</h1>
      <button onClick={() => bears.increase(1)}>INCREASE BEARS</button>
      <Link href="/about">
        <h1>ABOUT</h1>
      </Link>
    </>
  )
}
