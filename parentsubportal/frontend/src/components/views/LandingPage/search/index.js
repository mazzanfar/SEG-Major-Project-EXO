import React, {Component} from "react";

import "./style.scss";
import Popup from "./popup";

import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getTopics } from "../../../../actions/topics";
import { getPosts } from "../../../../actions/posts";
import { getDocuments } from "../../../../actions/documents";

RegExp.escape = function(s) {
  return s.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
};

export class Search extends Component {
    constructor(props) {
        super(props);

        this.handleClickOutside = this.handleClickOutside.bind(this);
        this.setWrapperRef = this.setWrapperRef.bind(this);

        this.state = {
            isPopupOpen: false,
            foundTopics: [],
            foundPosts: [],
            foundDocuments: [],
            errors: [],
            isError: false
        }
    }

    static propTypes = {
        topics: PropTypes.array.isRequired,
        posts: PropTypes.array.isRequired,
        documents: PropTypes.array.isRequired
    }

    componentDidMount() {
        this.props.getTopics();
        this.props.getPosts();
        this.props.getDocuments();
        document.addEventListener('mousedown', this.handleClickOutside);
    }

    componentWillUnmount() {
        document.addEventListener('mousedown', this.handleClickOutside);
    }

    setWrapperRef(node) {
        this.wrapperRef = node;
    }

    handleClickOutside(e) {
        if (this.wrapperRef && !this.wrapperRef.contains(e.target) && this.state.isPopupOpen) {
            this.hidePopup();
        }
    }

    searchWord(keyword) {
        keyword = RegExp.escape(keyword.toLowerCase());
        const pattern = `[A-Za-z.\s]*${keyword}[A-Za-z.\s]*`;
        const matchRegex = new RegExp(pattern);
        const foundTopics = this.props.topics.filter((item) => matchRegex.test(item.name.toLowerCase()))
        const foundPosts = this.props.posts.filter((item) => matchRegex.test(item.title.toLowerCase()))
        const foundDocuments = this.props.documents.filter((item) => matchRegex.test(item.title.toLowerCase()))

        this.setState({ foundTopics, foundPosts, foundDocuments })
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
        const { isPopupOpen, foundTopics, foundPosts, foundDocuments } = this.state;
        return (
            <div className="search">
                <div className="search-container">
                    <div className="title">Condition</div>
                    <div className="content">
                    <input ref={this.setWrapperRef}
                        type="text"
                        placeholder="Food"
                        onInput={this.onInput.bind(this)}
                        onChange={this.onInputChange.bind(this)}/>
                        <Popup
                            isOpen={isPopupOpen}
                            topics = {foundTopics}
                            posts = {foundPosts}
                            documents = {foundDocuments}
                        />
                    </div>
            </div>
        </div>
        );
    }
}

const mapStateToProps = state => ({
    topics: state.topics.topics,
    posts: state.posts.posts,
    documents: state.documents.documents
})

export default connect(mapStateToProps, {
    getTopics, getPosts, getDocuments } 
)(Search);
