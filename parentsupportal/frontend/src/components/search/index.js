import React, {Component} from "react";

import "./style.scss";
import Popup from "./popup";


import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getTopics } from '../../actions/topics';

RegExp.escape = function(s) {
  return s.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
};

export class Search extends Component {
    constructor(props) {
        super(props);
        this.state = {
            isPopupOpen: false,
            foundTopics: [],
            errors: [],
            isError: false
        }
    }
    static propTypes = {
        topics: PropTypes.array.isRequired
    }

    componentDidMount() {
        this.props.getTopics();
    }

    searchWord(keyword) {
        keyword = RegExp.escape(keyword.toLowerCase());
        const pattern = `[A-Za-z.\s]*${keyword}[A-Za-z.\s]*`;
        const matchRegex = new RegExp(pattern);
        const foundTopics = this.props.topics.filter((item) => matchRegex.test(item.name.toLowerCase()))
        this.setState({ foundTopics })
    }

    onInput(e) {
        if(e.target.value !== "") this.showPopup();
        else this.hidePopup();
    }

    onInputChange(e)  {
        const keyword = e.target.value;
        this.searchWord(keyword)
    }

    showPopup() {
        this.setState( { isPopupOpen: true });
    }

    hidePopup() {
        this.setState({ isPopupOpen: false});
    }

    setError(msg) {
        this.setState((prevState) => ({ errors: [...prevState.errors, msg], isError: true}))
    }

    clearAllErrors() {
        this.setState({ errors: [], isError: false})
    }
    render() {
        const { isPopupOpen, foundTopics } = this.state;
        return (
            <div className="search">
                <div className="search-container">
                    <div className="title">Condition</div>
                    <div className="content">
                    <input
                        type="text"
                        placeholder="Food"
                        onInput={this.onInput.bind(this)}
                        onChange={this.onInputChange.bind(this)}/>
                        <Popup
                            isOpen={isPopupOpen}
                            items = {foundTopics}
                        />
                    </div>
            </div>
        </div>
        );
    }
}

const mapStateToProps = state => ({
    topics: state.topics.topics
})

export default connect(mapStateToProps, { getTopics } )(Search);
