import React from 'react';
import { hot } from 'react-hot-loader';

class App extends React.Component {
    render() {
        return (
            <div>
                <h3>Hola chaval!</h3>
            </div>
        );
    }
}

export default hot(module)(App);