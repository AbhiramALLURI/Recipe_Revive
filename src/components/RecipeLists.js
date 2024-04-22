import React, { useEffect, useState } from 'react';
import { BsSearch } from 'react-icons/bs';
import { fetchData } from "../service";
import Modal from './modal'; // Ensure this path is correct
import SearchBar from './SearchBar'; // Ensure this path is correct
import NutritionList from './NutritionList'; // Ensure this path is correct

function RecipeLists(props) {
    const [searchedTerm, setSearchedTerm] = useState('');
    const [query, setQuery] = useState('pasta');
    const [data, setData] = useState('');
    const [showModal, setShowModal] = useState(false); // State for modal visibility
    const [selectedRecipe, setSelectedRecipe] = useState(null);
    const [selectedOption, setSelectedOption] = useState(''); // State for selected option

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

    const handleSelectRecipe = () => {
        setSelectedOption('recipe');
    };

    const handleSelectNutrition = () => {
        setSelectedOption('nutrition');
    };

    const handleRecipeClick = (recipe) => {
        setSelectedRecipe(recipe);
        setShowModal(true); // Show the modal when a recipe is clicked
    };

    const closeModal = () => {
        setShowModal(false);
    };

    return (
        <div className='container'>
            <div className='option-selector'>
                <button onClick={handleSelectRecipe}>Select Recipe</button>
                <button onClick={handleSelectNutrition}>Select Nutrition</button>
            </div>
            <>
                {selectedOption === 'recipe' && (
                    <>
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
                            {data && data.hits.map((item, index) => (
                                <div key={index} className='flexItem' onClick={() => handleRecipeClick(item.recipe)}>
                                    <div className='img-wrapper'>
                                        <img src={item.recipe.image} alt={item.recipe.label} />
                                    </div>
                                    <p>{item.recipe.label}</p>
                                </div>
                            ))}
                        </div>
                    </>
                )}
                {selectedOption === 'nutrition' && (
                    <NutritionList />
                )}
            </>
            {showModal && selectedRecipe && (
                <Modal recipe={selectedRecipe} onClose={closeModal} />
            )}
        </div>
    );
}

export default RecipeLists;