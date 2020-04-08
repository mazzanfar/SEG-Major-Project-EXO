import React, { Component } from 'react';
import { Container, Sidebar, Segment, Menu, Link, Icon } from "semantic-ui-react"
import PDFForm from './PDFForm';
import TraffiChart from './TrafficChart'

export class AdminPage extends Component {
    render() {
        return (
            <Container fluid>
                  <Sidebar.Pushable as={Segment}>
                    <Sidebar
                      as={Menu}
                      animation='push'
                      icon='labeled'
                      vertical
                      visible
                      width='thin'
                      color='grey'
                    >
                      <Menu.Header>Hi</Menu.Header>
                      <Menu.Menu>
                          <Menu.Item as='a'>
                            Home
                          </Menu.Item>
                          <Menu.Item as='a'>
                            Analytics
                          </Menu.Item>
                          <Menu.Item as='a'>
                            Resources
                          </Menu.Item>
                      </Menu.Menu>
                    </Sidebar>
                    <Sidebar.Pusher>
                    <Segment basic>
                        <TraffiChart/>
                        <PDFForm/>
                    </Segment>
                  </Sidebar.Pusher>
                </Sidebar.Pushable>
            </Container>
        )
    }
}

export default AdminPage;
