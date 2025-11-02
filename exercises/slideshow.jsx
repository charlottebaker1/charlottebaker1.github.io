import "../css/Slideshow.css";
import {useState} from "react";

const Slideshow = () => {
    const[slideIndex, setSlideIndex] = useState(0);

    const importAll = (resource) => {
        return resource.keys().map(resource);
    };

    const images = importAll(
        require.context("../images/slideshow", false, /\.(png|jpe?g|svg$|webp)/)
    );

    const slideForward = () => {
        if (slideIndex < images.length -1){
            setSlideIndex(slideIndex+1);
        } else {
            setSlideIndex(0);
        }
            
    };

        const slideBackward = () => {
        if (slideIndex > 0){
            setSlideIndex(slideIndex-1);
        } else {
            setSlideIndex(images.length-1);
        }

            
    };


    setSlideIndex(slideIndex < images.length)

    return(
        <section id="slideshow">
            <img src={images[slideIndex]} />
            <a className="arrow" id="right-arrow" href="#">&gt;</a>
            <a className="arrow" id="left-arrow" href="#">&lt;</a>
        </section>
    );
}

export default Slideshow;
    