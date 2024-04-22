import React, { Component, useState } from 'react';
import './App.scss';
import Header from './components/Header';
import Tabs from './components/Tabs';
import RecipeLists from './components/RecipeLists';
import SearchBar from './components/SearchBar';
import NutritionList from './components/NutritionList';
import Exp from './components/Exp';


const App = () => {
  const [foods, setFoods] = useState([]);
  const [loader, setLoader] = useState(true);
  const [selectedOption, setSelectedOption] = useState('');
  const handleOptionChange = (option) => {
    setSelectedOption(option);
};

return (
  <div className="main">
    <Header />
    <Tabs setLoader={setLoader}/>
    <RecipeLists setLoader={setLoader}/>
    {loader && <div className='loader'>
      <div className='spinner'></div>
      </div>}
    <Exp>
      
    </Exp>
  </div>
);
}

export default App;

//sdvsd