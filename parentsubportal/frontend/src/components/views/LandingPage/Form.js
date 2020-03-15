import React, { Component } from "react";
import { connect } from "react-redux";
import axios from 'axios';
import PropTypes from "prop-types";
import { addPost } from "../../../actions/posts";
import { getUser } from "../../../actions/auth";

export class Form extends Component {
    state = {
        title: "",
        content: "",
        author: 0
    };

    static propTypes = {
        addPost: PropTypes.func.isRequired
    };

    componentDidMount() {
        this.props.getUser();
        axios
        .get(`/api/auth/user`)
        .then(res => {
            const author = res.data.id
            this.setState({author});
        })
        .catch(err => console.log(err));
    }

    onChange = e => this.setState({ [e.target.name]: e.target.value });
    
    onSubmit = e => {
        e.preventDefault();
        const { title, content, author } = this.state;
        const post = { title, content, author};
        //console.log(user.id);
        this.props.addPost(post);
        this.setState({
            title: "",
            content: ""
        });
    };
    
    render() {
        const { title, content } = this.state;
        return (
          <div className="card card-body mt-4 mb-4">
            <h2>Add Post</h2>
            <form onSubmit={this.onSubmit}>
              <div className="form-group">
                <label>Name</label>
                <input
                  className="form-control"
                  type="text"
                  name="title"
                  onChange={this.onChange}
                  value={title}
                />
              </div>
              <div className="form-group">
                <label>Content</label>
                <textarea
                  className="form-control"
                  type="text"
                  name="content"
                  onChange={this.onChange}
                  value={content}
                />
              </div>
              <div className="form-group">
                <button type="submit" className="btn btn-primary">
                  Submit
                </button>
              </div>
            </form>
          </div>
        );
    }
}

const mapStateToProps = state => ({
    user: state.user.user
});

export default connect(
    null,
    { addPost, getUser }
)(Form);
