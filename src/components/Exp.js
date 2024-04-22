import React, { useState, useEffect } from 'react';

function Exp() {
  const [foodItem, setFoodItem] = useState('');
  const [expirationDate, setExpirationDate] = useState('');
  const [reminderDays, setReminderDays] = useState(3);
  const [reminders, setReminders] = useState([]);

  useEffect(() => {
    checkExpirationDates();
  }, [reminders]);

  const checkExpirationDates = () => {
    reminders.forEach(reminder => {
      const expiration = new Date(reminder.expirationDate);
      const today = new Date();
      const diffTime = expiration.getTime() - today.getTime();
      const diffDays = Math.ceil(diffTime / (1000 * 3600 * 24));

      if (diffDays <= reminder.reminderDays) {
        showNotification(reminder.foodItem, reminder.expirationDate);
      }
    });
  };

  const showNotification = (foodItem, expirationDate) => {
    if ('Notification' in window) {
      Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
          const options = {
            body: `The expiration date for ${foodItem} is near (${expirationDate}).`,
            icon: 'path_to_your_icon.png'
          };
          new Notification('Food Expiration Reminder', options);
        }
      });
    }
  };

  const handleAddReminder = () => {
    if (foodItem && expirationDate) {
      const newReminder = {
        id: Math.random(),
        foodItem,
        expirationDate,
        reminderDays
      };
      setReminders([...reminders, newReminder]);
      setFoodItem('');
      setExpirationDate('');
    } else {
      alert('Please fill in all fields.');
    }
  };

  const handleDeleteReminder = id => {
    const updatedReminders = reminders.filter(reminder => reminder.id !== id);
    setReminders(updatedReminders);
  };

  return (
    <div className="Exp">
      <h1>Food Expiration Reminder</h1>
      <div className="add-reminder">
        <input
          type="text"
          placeholder="Food Item"
          value={foodItem}
          onChange={e => setFoodItem(e.target.value)}
        />
        <input
          type="date"
          value={expirationDate}
          onChange={e => setExpirationDate(e.target.value)}
        />
        <select
          value={reminderDays}
          onChange={e => setReminderDays(parseInt(e.target.value))}
        >
          <option value={1}>1 Day Before</option>
          <option value={2}>2 Days Before</option>
          <option value={3}>3 Days Before</option>
          <option value={7}>1 Week Before</option>
        </select>
        <button onClick={handleAddReminder}>Add Reminder</button>
      </div>
      <div className="reminders">
        {reminders.map(reminder => (
          <div className="reminder" key={reminder.id}>
            <span>{reminder.foodItem}</span>
            <span>Expires on: {reminder.expirationDate}</span>
            <span>Reminder: {reminder.reminderDays} days before</span>
            <button onClick={() => handleDeleteReminder(reminder.id)}>Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Exp;
//Expiration remainder

