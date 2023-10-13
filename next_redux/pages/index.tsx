import Image from 'next/image'
import { Inter } from 'next/font/google'
import { useDispatch, useSelector } from 'react-redux'
import { Root } from 'postcss'
import { AppDispatch, RootState } from '@/store/store'
import { fetch, increment } from '@/slices/counterSlice'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const count = useSelector((state: RootState) => state.counter.value)
  const dispatch = useDispatch<AppDispatch>();
  return (
    <>
    <h1>{count}</h1>
    <button onClick={() => dispatch(increment())}>ADD ONE</button>
    <button onClick={() => dispatch(fetch())}>ASYNC ADD</button>
    </>
  )
}
