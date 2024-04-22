import React, { useState, useEffect } from 'react';
import Chart from 'chart.js/auto';

function NutritionList() {
  const [title, setTitle] = useState('');
  const [recipe, setRecipe] = useState('');
  const [nutritionData, setNutritionData] = useState(null);

  useEffect(() => {
    // Function to create the pie chart
    const createPieChart = (data) => {
      const ctx = document.getElementById('nutrient-chart').getContext('2d');
      new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['Calories', 'Energy', 'Fat', 'Carbs', 'Fiber', 'Protein', 'Calcium'],
          datasets: [{
            label: 'Nutrient Information',
            data: [
              data.calories,
              data.totalNutrients.ENERC_KCAL ? data.totalNutrients.ENERC_KCAL.quantity.toFixed(2) : 0,
              data.totalNutrients.FAT ? data.totalNutrients.FAT.quantity.toFixed(2) : 0,
              data.totalNutrients.CHOCDF ? data.totalNutrients.CHOCDF.quantity.toFixed(2) : 0,
              data.totalNutrients.FIBTG ? data.totalNutrients.FIBTG.quantity.toFixed(2) : 0,
              data.totalNutrients.PROCNT ? data.totalNutrients.PROCNT.quantity.toFixed(2) : 0,
              data.totalNutrients.CA ? data.totalNutrients.CA.quantity.toFixed(2) : 0,
            ],
            backgroundColor: [
              '#ff6384', // Red for Calories
              '#36a2eb', // Blue for Energy
              '#ffce56', // Yellow for Fat
              '#4bc0c0', // Green for Carbs
              '#9966ff', // Purple for Fiber
              '#ffcc99', // Orange for Protein
              '#ff99cc'  // Pink for Calcium
            ],
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          aspectRatio: 1.5,
          plugins: {
            title: {
              display: true,
              text: 'Nutrient Information',
              fontSize: 18
            }
          }
        }
      });
    };

    if (nutritionData) {
      createPieChart(nutritionData);
    }
  }, [nutritionData]);

  const fetchRecipe = async () => {
    const appId = '361742a2';
    const apiKey = 'ad54356419621387cd0511ac8a7654ac';
    const ingr = recipe.split('\n');
    const url = `https://api.edamam.com/api/nutrition-details?app_id=${appId}&app_key=${apiKey}`;
    
    try {
      const response = await fetch(url, {
        method: 'POST',
        cache: 'no-cache',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, ingr })
      });
      const data = await response.json();
      setNutritionData(data);
    } catch (error) {
      console.error('Error fetching nutrition data:', error);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetchRecipe();
  };

  return (
    <div>
      <nav className="navbar navbar-dark bg-dark">
        <div className="container">
          <a className="navbar-brand">
            Nutrition Info
          </a>
        </div>
      </nav>
      <div className="container mt-3">
        <div className="row">
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="title" className="form-lable"> Title</label>
              <input 
                type="text" 
                className="form-control" 
                id="title" 
                name="title" 
                value={title} 
                onChange={(e) => setTitle(e.target.value)} 
              />
            </div>
            <div className="mb-3">
              <label htmlFor="recipe" className="form-label"> Recipe</label>
              <textarea 
                className="form-control" 
                id="recipe" 
                name="recipe" 
                rows="3" 
                value={recipe} 
                onChange={(e) => setRecipe(e.target.value)} 
              />
            </div>
            <button className="btn btn-primary">Submit Recipe</button>
          </form>
        </div>
        <div className="row mt-3">
          <canvas id="nutrient-chart"></canvas>
        </div>
      </div>
    </div>
  );
}

export default NutritionList;