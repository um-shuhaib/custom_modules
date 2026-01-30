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
            categories:[],
            products:[],
            activeCat:null,
            activeCatName:"No Category Selected",
            page:1,
            limit:6,
            total:0,
        });

        onWillStart(async ()=>{
            // this.state.categoies=await this.orm.search_read('product.category',[],['id','name']);
            this.state.categories=await this.orm.call('product.category',
                'search_read',
                [[],['id','name']]
            );
        });
    }

    async selectCategory(categoryId,categoryName){
        this.state.activeCat=categoryId;
        this.state.activeCatName=categoryName;
        this.state.page=1;
        await this.loadProducts()
        // this.state.products=await this.orm.call("product.product",
        //     "search_read",
        //     [],
        //     {
        //         domain:[['categ_id','=',categoryId]],
        //         fields:['id','name']
        //     }
        // );
    }

    increment(){
        this.state.value++;
    }
    decrement(){
        if (this.state.value > 0){
            this.state.value--;
        }
    }

    async loadProducts(){
        const offset = (this.state.page - 1) * this.state.limit;

        this.state.total=await this.orm.call(
            'product.product',
            'search_count',
            [[['categ_id','=',this.state.activeCat]]]
            
        );


        this.state.products=await this.orm.call(
            'product.product',
            'search_read',
            [],
            {
                domain:[['categ_id','=',this.state.activeCat]],
                fields:['id','name','qty_available'],
                limit:this.state.limit,
                offset:offset
            }
        );
    }

    async nextPage(){
        const maxPage=Math.ceil(this.state.total / this.state.limit)
        if (this.state.page < maxPage){
            this.state.page++;
            await this.loadProducts();
        }
    }

    async prePage(){
        if (this.state.page > 1){
            this.state.page--;
            await this.loadProducts();
        }
    }


    }
NewField.template = 'owl_module.TodoList'

registry.category("actions").add("owl_module.todo_list",NewField)