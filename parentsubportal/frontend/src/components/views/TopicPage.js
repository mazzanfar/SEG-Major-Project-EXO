import React, {Component} from 'react'
import { withRouter } from 'react-router-dom'

class TopicPage extends Component {
    render() {
        return (
            <p>{this.props.match.params.topic}</p>
        )
    }
}

export default withRouter(TopicPage);
