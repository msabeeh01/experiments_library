import Image from 'next/image'
import { Inter } from 'next/font/google'
import { usePlaidLink } from 'react-plaid-link'
import { useCallback, useEffect, useState } from 'react'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const [linkToken, setLinkToken] = useState(null)

  const generateToken = async () => {
    try{
      const response = await fetch('http://127.0.0.1:5000/create_link_token', {
        method: 'POST',
      })
      const data = await response.json()
      setLinkToken(data.link_token)
    }catch(e){
      console.log(e)
    }

  }

  useEffect(() => {
    generateToken()
  }, [])

  return linkToken != null ? <Link linkToken={linkToken} /> : <p>Loading</p>
}

const Link = (props) => {
  const onSuccess = useCallback((public_token, metadata) => {
    // send public_token to server
    const response = fetch('http://127.0.0.1:5000/exchange_public_token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ public_token }),
    });

    return(
      <Accounts />
    )
    // Handle response ...
  }, []);
  const config = {
    token: props.linkToken,
    // receivedRedirectUri: window.location.href,
    onSuccess,
  };
  const { open, ready } = usePlaidLink(config);
  return (
    <button onClick={() => open()} disabled={!ready}>
      Link account
    </button>
  );
};

const Accounts = (props) => {
  const [accounts, setAccounts] = useState(null)

  useEffect(() => {
    getAccounts()
  }, [])

  const getAccounts = async () => {
    try{
      const response = await fetch('http://127.0.0.1:5000/accounts', {
        method: 'GET',
      })
      const data = await response.json()
      console.log(data)
      setAccounts(data.accounts)
    }catch(e){
      console.log(e)
    }

    return(
      <>
        {accounts}
      </>
    )
}
}