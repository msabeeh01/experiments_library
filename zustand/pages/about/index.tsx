import { useBearStore } from "@/stores/bearStore"
import { useEffect } from "react"

const About = () =>{
    const bears = useBearStore()
    useEffect(()=>{
        bears.fetch();
    },[])
    return(
        <>
            <h1>{bears.bears}</h1>
        </>
    )
}

export default About