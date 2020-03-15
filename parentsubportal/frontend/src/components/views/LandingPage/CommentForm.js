import React, { Component } from 'react';
import axios from 'axios';
import { Button, Form, Message } from 'semantic-ui-react'
import {postComment} from "../../../actions/comments"
import {connect} from 'react-redux'

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class CommentForm extends Component {
    state = {
        content: "",
    }

    handleSubmit = (e) => {
        e.preventDefault();
        const comment = {'post': this.props.post.id, 'content': this.state.content, 'author': 15} 
        console.log(comment)
        this.props.postComment(comment)
    }

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    };

    render() {
        return (
            <Form reply onSubmit={this.handleSubmit}>
                <Form.TextArea required id="content" value={this.state.content} onChange={this.handleChange}/>
                <Button content="Add Reply" labelPosition="left" icon="edit" primary />
            </Form>
        );
    }
}
export default connect(
    null,
    {postComment}
)(CommentForm);
