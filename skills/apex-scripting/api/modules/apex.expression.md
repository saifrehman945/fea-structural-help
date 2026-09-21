# apex.expression

Apex release: Iberian Lynx FP2. All arguments are keyword-only.

## Module functions

### `apex.expression.bind(target: apex.Entity, attribute: str, expression: str, updateAfterBind: bool = True) -> bool`
Binds the value of an object property to an expression. Apex enables object properties to be defined directly, using value types or instances of objects or indirectly using expressions. An Apex expression is defined using a string that represents any valid single line Python statement. The expression string must start wit the "=" character. For example, expression = '=15.0*(23.6/120.0)' The expression must return a type that matches the object property type that the expression is bound to. Expressions may include references to Apex objects or object properties. To reference an Apex object within an expression the object must be identified using it's minimally unique path and Name. For example, to identify the location of a geometry solid name "Con rod", the following expression could be defined expression = '=@("Con rod").location' although this expression would ONLY be valid if there was a single named entity within the active Apex session that used the name "Con rod". To ensure unique identification of an object the full pathName of the object can be used. For example, expression = '=@("MyModel/MyAssembly/MyPart/Con rod").location' The method will raise an exception if the expression cannot be successfully evaluated.

- `target` — The target entity that composes the property that the expression will bind to.
- `attribute` — The name of the attribute on the target entity that will be bound to the expression.
- `expression` — A valid Python expression. When evaluated, this expression must return a type that matches the type of the named attribute on the target entity.
- `updateAfterBind` — A boolean value. When the value is True at the last of bind operation target related attribute will be update by the expression, or else don't do update

Returns: true is bound, false is not bound

### `apex.expression.bulkbind(target: apex.Entity, attributeToExpressionMap: {str:str}, updateAfterBind: bool = True) -> bool`
Binds the values of the object properties to the expressions, the object properties and the expressions are stroed in a map . Apex enables object properties to be defined directly, using value types or instances of objects or indirectly using expressions. An Apex expression is defined using a string that represents any valid single line Python statement. The expression string must start wit the "=" character. For example, expression = '=15.0*(23.6/120.0)' The expression must return a type that matches the object property type that the expression is bound to. Expressions may include references to Apex objects or object properties. To reference an Apex object within an expression the object must be identified using it's minimally unique path and Name. For example, to identify the location of a geometry solid name "Con rod", the following expression could be defined expression = '=@("Con rod").location' although this expression would ONLY be valid if there was a single named entity within the active Apex session that used the name "Con rod". To ensure unique identification of an object the full pathName of the object can be used. For example, expression = '=@("MyModel/MyAssembly/MyPart/Con rod").location' The method will raise an exception if the expression cannot be successfully evaluated.

- `target` — The target entity that composes the property that the expression will bind to.
- `attributeToExpressionMap` — The map of the attribute name and the expression, the ttribute name will bind to the expression.
- `updateAfterBind` — A boolean value. When the value is True at the last of bind operation target related attribute will be update by the expression, or else don't do update

Returns: true is bound, false is not bound

