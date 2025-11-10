

const House = (props) => {
    return (
        <section className="house">
            <img src={"https://portiaportia.github.io/json/images/house-plans/"+props.main_image} alt="house" />
            <div className="house-description">
                <h1>{props.name}</h1>
                <p>Num Bedrooms: {props.bedrooms}</p>
            </div>
        </section>
    );
};

export default House;