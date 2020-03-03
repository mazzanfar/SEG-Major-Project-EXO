import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Search from "../components/search";

import { Provider } from "react-redux";
import store from "../store";


class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <div className="container">
                    <Search />
                </div>
            </Provider>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
