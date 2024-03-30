import React, { useEffect, useState } from 'react';
import { BsSearch } from 'react-icons/bs';
import { fetchData } from "../service";
import Modal from './modal';
function RecipeLists(props) {
    const [searchedTerm, setSearchedTerm] = useState('');
    const [query, setQuery] = useState('pasta');
    const [data, setData] = useState('');
    const [showIngredients, setShowIngredients] = useState(false);
    const [selectedRecipe, setSelectedRecipe] = useState(null);
    
    
    const searchRecipe = (searchQuery) => {
        fetchData(searchQuery).then((response) => {
            setData(response);
            props.setLoader(false);
        });
    };
    

    useEffect(() => {
        fetchData(query).then((response) => {
            setData(response);
            props.setLoader(false);
        });
    }, []);

    const handleRecipeClick = (recipe) => {
        setSelectedRecipe(recipe);
        setShowIngredients(true);
    };

    return (
        <div className='container'>
            <div className='heading-line'>
                <strong>Search Recipes</strong>
                <div className='input-wrapper'>
                    <input
                        onChange={(e) => setSearchedTerm(e.target.value)}
                        value={searchedTerm}
                        type="text"
                        placeholder='Search your recipe' />
                    <button onClick={() => (searchRecipe(searchedTerm), props.setLoader(true))}><BsSearch /></button>
                </div>
            </div>
            <div className='flexbox'>
                {
                    data && data.hits.map((item, index) => (
                        <div key={index} className='flexItem' onClick={() => handleRecipeClick(item.recipe)}>
                            <div className='img-wrapper'>
                                <img src={item.recipe.image} alt={item.recipe.label} />
                            </div>
                            <p>{item.recipe.label}</p>
                        </div>
                    ))
                }
            </div>
            {showIngredients && selectedRecipe && (
        <Modal isOpen={showIngredients} onClose={() => setShowIngredients(false)}>
            <h3>Ingredients for {selectedRecipe.label}</h3>
            <ul>
                {selectedRecipe.ingredients.map((ingredient, index) => (
                    <li key={index}>{ingredient.text}</li>
                ))}
            </ul>
        </Modal>
    )}
        </div>
    );
}



export default RecipeLists;
