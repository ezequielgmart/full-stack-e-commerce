

class Query():

    """ GENERADORES DE LAS QUERIES """
    # quiero que mediante los parametros me genere la query
    def generate(self, gem, type:str, limit:bool, offset:bool, fields:str = "ALL", where:str = None) -> str:

        table = gem.get_table()

        if fields == "ALL":
            table_fields = gem.get_all_table_fields()

            table_fields_to_string = gem.convert_fields_to_string(table_fields)
        
            if type == "SELECT": 
                  
                query = self.select_query(
                    query_type=type,
                    table=table, 
                    table_fields_to_string=table_fields_to_string,
                    where=where,
                    limit=limit, 
                    offset=offset
                    )
                
                print(query)
                return query
            
            # if type=="INSERT": 
            
            #     pass 

            
            # if type=="UPDATE": 
            
            #     pass 
            
            # if type=="DELETE": 
            
            #     pass         
            
class Query():
    # ... otros métodos ...
        
    def generate_join(
        self,
        main_gem,
        main_fields: list[str],
        join_gems: list[dict],
        where_field: str = None
    ) -> str:
        
        main_table = main_gem.get_table()
        main_alias = main_gem.get_alias()

        select_clauses = [f"{main_alias}.{field}" for field in main_fields]
        join_clauses = []
        group_by_fields = [f"{main_alias}.{field}" for field in main_fields]

        # Mapeo de alias para las uniones
        alias_map = {
            main_gem.get_table(): main_alias
        }
        
        # Recorre las uniones para construir las cláusulas
        for item in join_gems:
            join_gem = item.get("gem")
            fields_to_join = item.get("fields")
            on_key = item.get("on_key")
            on_with = item.get("on_with")

            join_table = join_gem.get_table()
            join_alias = join_gem.get_alias()
            alias_map[join_table] = join_alias

            # Lógica para manejar ARRAY_AGG de imágenes
            if join_table == 'images':
                # La unión de 'images' usa la tabla de unión 'product_images'
                product_images_alias = alias_map.get('product_images')
                join_clause = (
                    f"LEFT JOIN {join_table} AS {join_alias} "
                    f"ON {product_images_alias}.{on_with} = {join_alias}.{on_key}"
                )
                join_clauses.append(join_clause)
                select_clauses.append(f"ARRAY_AGG(DISTINCT {join_alias}.image_url) AS image_urls")

            # Lógica para la tabla de unión de imágenes, que se une a la tabla principal 'products'
            elif join_table == 'product_images':
                join_clause = (
                    f"LEFT JOIN {join_table} AS {join_alias} "
                    f"ON {main_alias}.{on_with} = {join_alias}.{on_key}"
                )
                join_clauses.append(join_clause)

            # Lógica para las otras uniones
            else:
                on_table_alias = alias_map.get(on_with)
                join_clause = (
                    f"LEFT JOIN {join_table} AS {join_alias} "
                    f"ON {on_table_alias}.{on_key} = {join_alias}.{on_key}"
                )
                join_clauses.append(join_clause)
                
                # Agrega los campos seleccionados y para GROUP BY
                for field in fields_to_join:
                    aliased_field = f"{join_alias}.{field}"
                    select_clauses.append(aliased_field)
                    group_by_fields.append(aliased_field)
        
        select_string = ", ".join(select_clauses)
        join_string = " ".join(join_clauses)
        group_by_string = ", ".join(group_by_fields)

        query_parts = [
            f"SELECT {select_string}",
            f"FROM {main_table} AS {main_alias}",
            join_string,
        ]

        if where_field:
            query_parts.append(f"WHERE {main_alias}.{where_field} = $1")

        query_parts.append(f"GROUP BY {group_by_string}")
        
        return " ".join(query_parts)
        

    def select_query(self, query_type:str, table:str, table_fields_to_string:str, limit:bool, offset:bool, where:str = None) -> str:

        if where is not None:

            if limit and offset:
                query_string = f"{query_type} {table_fields_to_string} FROM {table} WHERE {where} = $1 LIMIT $2 OFFSET $3"
                return query_string
            
            else: 
                
                query_string = f"{query_type} {table_fields_to_string} FROM {table} WHERE {where} = $1"
                return query_string

            # else: 
            #     query_string = f"{query_type} {table_fields_to_string} FROM {table} WHERE {where} = $1"
            #     return query_string
                
        else:
            
            query_string = f"{query_type} {table_fields_to_string} FROM {table}"

            return query_string

    def insert_query(self, query_type:str, table:str, table_fields_to_string:str):
        pass 

    def update_query(self, query_type:str, table:str, table_fields_to_string:str, where:str):
        pass 

    def delete_query(self, query_type:str, table:str, table_fields_to_string:str, where:str):
        pass 


    """ METODOS PARA PREPARAR QUERYS, LIMPIAR DATOS, ENTRE OTROS QUE NO SON LOS DE GENERAR EL STRING FINAL """
    
    def generate_join_string(
            self, 
            main_table:str, 
            main_alias:str, 
            join_alias:str, 
            where_field:str) -> str:
        
        join_clause = f"JOIN {main_table} AS {main_alias} ON {join_alias}.{where_field} = {main_alias}.{where_field}"

        return join_clause
    
    def set_fields_for_join_query(self, fields:list[str], alias:str) -> str: 

        fields_with_alias =  self.add_alias_to_fields(fields=fields, alias=alias)

        return self.convert_fields_to_string(fields_with_alias) # returns an string of fields with the alias added
    
            
    def add_alias_to_fields(self, fields:list[str], alias:str) -> str:

        # le agregara el alias de la tabla a cada campo. 
        return [f"{alias}.{field}" for field in fields]
    
    def convert_fields_to_string(self, fields: list[str]) -> str:
        return ', '.join(fields)
                
def main() -> str:

    return "Hello World"


if __name__ == "__main__":

    main()