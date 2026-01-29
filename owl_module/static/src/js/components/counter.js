/** @odoo-module **/
import {registry} from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
// const {Component,useState} = owl;

export class NewField extends Component{
    setup(){
        this.orm=useService("orm")
        this.state = useState({
            value:0,
            categories:[]
        });

        onWillStart(async ()=>{
            // this.state.categoies=await this.orm.search_read('product.category',[],['id','name']);
            this.state.categories=await this.orm.call('product.category','search_read',[[],['id','name']]);
        });
    }

    increment(){
        this.state.value++;
    }
    decrement(){
        if (this.state.value > 0){
            this.state.value--;
        }
    }


    }
NewField.template = 'owl_module.TodoList'

registry.category("actions").add("owl_module.todo_list",NewField)